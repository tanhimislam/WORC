from WORC.validators import AbstractValidator
from WORC.processing.label_processing import load_label_csv
import WORC.addexceptions as ae

# Global variables

min_subjects = 10
recommended_subjects = 50





class SimpleValidator(AbstractValidator):
    def _validate(self, simpleworc, *args, **kwargs):
        if not simpleworc._method:
            raise ae.WORCValueError(
                f'No method selected. Call function binary_classification(**) or regression(**) or survival(**) on SimpleWorc().')

        if simpleworc._images_train:
            for num, (ims, segs) in enumerate(zip(simpleworc._images_train, simpleworc._segmentations_train)):
                if ims.keys() != segs.keys():
                    raise ae.WORCValueError(
                        f'Subjects in images_train and segmentations_train are not the same for modality {num}.')

        if simpleworc._method == 'survival':
            self._validate_survival(simpleworc, *args, **kwargs)
        else:
            if not simpleworc._labels_file_train:
                raise ae.WORCValueError(f'No labels, use SimpleWorc().labels_from_this_file(**) to add labels.')

            if not simpleworc._label_names:
                raise ae.WORCValueError(f'No label(s) to predict selected. Use SimpleWorc().predict_labels(**) to select labels.')

    def _validate_survival(self, simpleworc, *args, **kwargs):
        pass

class MinSubjectsValidator(AbstractValidator):
    def _validate(self, simpleworc, *args, **kwargs):
        if simpleworc._num_subjects < min_subjects:
            raise ae.WORCValueError(f'Less than {min_subjects} subjects (you have {simpleworc._num_subjects}) will probably make WORC crash due to a split in the test/validation set having only one subject. Use at least {min_subjects} subjects or more.')


class SamplesWarning(AbstractValidator):
    # Not really a validator, but more a good practice. Hence this won't throw an exception but prints a warning instead.
    def _validate(self, simpleworc, *args, **kwargs):
        if simpleworc._method == 'classification':
            if simpleworc._num_subjects < len(simpleworc._label_names) * recommended_subjects: # at least 100 subjects per label recommended
                print(f'Warning: at least {len(simpleworc._label_names) * recommended_subjects} subjects is recommended when predicting {len(simpleworc._label_names)} labels. Current subject count is: {simpleworc._num_subjects}')
        elif simpleworc._method == 'regression':
            # TODO @martijn not sure how to tackle this, what would be a reasonable amount of subjects for regression?
            pass


class InvalidLabelsValidator(AbstractValidator):
    def _validate(self, simpleworc):
        try:
            labels, subjects, _ = load_label_csv(simpleworc._labels_file_train)
        except ae.WORCAssertionError as wae:
            if 'First column should be patient ID' in str(wae):
                # TODO: print wrong column name and file so that it is clear what needs to be replaced in which file
                raise ae.WORCValueError(f'First column in the file given to SimpleWORC().labels_from_this_file(**) needs to be named Patient.')

        # check labels for substrings of eachother
        labels_matches = self._get_all_substrings_for_array(labels)

        if labels_matches:
            # if not empty we have a problem
            errstr = "Found label(s) that are a substring of other label(s). This is currently not allowed in WORC. Rename the following label(s):\n"
            for label, matches in labels_matches.items():
                for match in matches:
                    errstr += f"{label} is a substring of {match}\n"

        # check subject names for substrings of eachother
        subjects_matches = self._get_all_substrings_for_array(subjects)
        if labels_matches:
            # if not empty we have a problem
            errstr = "Found subject(s) that are a substring of other subject(s). This is currently not allowed in WORC. Rename the following subject(s):\n"
            for subject, matches in subjects_matches.items():
                for match in matches:
                    errstr += f"{label} is a substring of {match}\n"

        if errstr:
            raise ae.WORCValueError(errstr)

    def _get_all_substrings_for_array(self, arr):
        # generate a dict with substrings of each element in array
        all_matches = {}
        for strcmp in arr:
            matches = [s for s in arr if s != strcmp and strcmp in s]
            if matches:
                all_matches[strcmp] = matches

        return all_matches


class ValidatorsFactory:
    @staticmethod
    def factor_validators():
        return [
            SimpleValidator(),
            MinSubjectsValidator(),
            SamplesWarning()
        ]


__all__ = [ValidatorsFactory]
