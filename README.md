# WORC v3.5.0
## Workflow for Optimal Radiomics Classification

## Information

| Unit test                      | Documentation                 | PyPi                          |Citing WORC          |
|--------------------------------|-------------------------------|-------------------------------|---------------------|
| [![][gi-workflow]][gi-workflow-lnk]  | [![][doc]][doc-lnk]           | [![][pypi]][pypi-lnk]         | [![][DOI]][DOI-lnk] |

[gi-workflow]: https://github.com/MStarmans91/WORC/workflows/Unit%20test/badge.svg
[gi-workflow-lnk]: https://github.com/MStarmans91/WORC/actions?query=workflow%3A%22Unit+test%22

[doc]:https://readthedocs.org/projects/worc/badge/?version=latest
[doc-lnk]: https://worc.readthedocs.io/en/latest/?badge=latest

[pypi]: https://badge.fury.io/py/WORC.svg
[pypi-lnk]: https://badge.fury.io/py/WORC

[DOI]: https://zenodo.org/badge/DOI/10.5281/zenodo.3840534.svg
[DOI-lnk]: https://zenodo.org/badge/latestdoi/92295542

# Introduction

WORC is an open-source python package for the easy execution and fully automatic construction and optimization of radiomics workflows.

<img src="images/WORC.jpg" alt="Overview"/>

We aim to establish a general radiomics platform supporting easy integration of other tools. With our modular build
and support of different software languages (python, MATLAB, ruby, java etc.), we want to facilitate and stimulate
collaboration, standardisation and comparison of different radiomics approaches. By combining this in a single framework,
we hope to find a universal radiomics strategy that can address various problems.

## License
This package is covered by the open source [APACHE 2.0 License](APACHE-LICENSE-2.0).

When using WORC, please cite this repository and the paper describing WORC as as follows:

```bibtex
@article{starmans2021reproducible,
   title={Reproducible radiomics through automated machine learning validated on twelve clinical applications}, 
   author={Martijn P. A. Starmans and Sebastian R. van der Voort and Thomas Phil and Milea J. M. Timbergen and Melissa Vos and Guillaume A. Padmos and Wouter Kessels and David    Hanff and Dirk J. Grunhagen and Cornelis Verhoef and Stefan Sleijfer and Martin J. van den Bent and Marion Smits and Roy S. Dwarkasing and Christopher J. Els and Federico Fiduzi and Geert J. L. H. van Leenders and Anela Blazevic and Johannes Hofland and Tessa Brabander and Renza A. H. van Gils and Gaston J. H. Franssen and Richard A. Feelders and Wouter W. de Herder and Florian E. Buisman and Francois E. J. A. Willemssen and Bas Groot Koerkamp and Lindsay Angus and Astrid A. M. van der Veldt and Ana Rajicic and Arlette E. Odink and Mitchell Deen and Jose M. Castillo T. and Jifke Veenland and Ivo Schoots and Michel Renckens and Michail Doukas and Rob A. de Man and Jan N. M. IJzermans and Razvan L. Miclea and Peter B. Vermeulen and Esther E. Bron and Maarten G. Thomeer and Jacob J. Visser and Wiro J. Niessen and Stefan Klein},
   year={2021},
   eprint={2108.08618},
   archivePrefix={arXiv},
   primaryClass={eess.IV}
}

@software{starmans2018worc,
  author       = {Martijn P. A. Starmans and Thomas Phil and Sebastian R. van der Voort and Stefan Klein},
  title        = {Workflow for Optimal Radiomics Classification (WORC)},
  year         = {2018},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.3840534},
  url          = {https://github.com/MStarmans91/WORC}
}
```

For the DOI, visit [![][DOI]][DOI-lnk].

## Disclaimer
This package is still under development. We try to thoroughly test and evaluate every new build and function, but
bugs can off course still occur. Please contact us through the channels below if you find any and we will try to fix
them as soon as possible, or create an issue on this Github.

## Tutorial, documentation and dataset
The WORC tutorial is hosted at https://github.com/MStarmans91/WORCTutorial.

The official documentation can be found at [https://worc.readthedocs.io](https://worc.readthedocs.io).

The publicly released WORC database is described in the following paper:

```bibtex
@article {Starmans2021.08.19.21262238,
	author = {Starmans, Martijn P.A. and Timbergen, Milea J.M. and Vos, Melissa and Padmos, Guillaume A. and Gr{\"u}nhagen, Dirk J. and Verhoef, Cornelis and Sleijfer, Stefan and van Leenders, Geert J.L.H. and Buisman, Florian E. and Willemssen, Francois E.J.A. and Koerkamp, Bas Groot and Angus, Lindsay and van der Veldt, Astrid A.M. and Rajicic, Ana and Odink, Arlette E. and Renckens, Michel and Doukas, Michail and de Man, Rob A. and IJzermans, Jan N.M. and Miclea, Razvan L. and Vermeulen, Peter B. and Thomeer, Maarten G. and Visser, Jacob J. and Niessen, Wiro J. and Klein, Stefan},
	title = {The WORC database: MRI and CT scans, segmentations, and clinical labels for 930 patients from six radiomics studies},
	elocation-id = {2021.08.19.21262238},
	year = {2021},
	doi = {10.1101/2021.08.19.21262238},
	publisher = {Cold Spring Harbor Laboratory Press},
	abstract = {The WORC database consists in total of 930 patients composed of six datasets gathered at the Erasmus MC, consisting of patients with: 1) well-differentiated liposarcoma or lipoma (115 patients); 2) desmoid-type fibromatosis or extremity soft-tissue sarcomas (203 patients); 3) primary solid liver tumors, either malignant (hepatocellular carcinoma or intrahepatic cholangiocarcinoma) or benign (hepatocellular adenoma or focal nodular hyperplasia) (186 patients); 4) gastrointestinal stromal tumors (GISTs) and intra-abdominal gastrointestinal tumors radiologically resembling GISTs (246 patients); 5) colorectal liver metastases (77 patients); and 6) lung metastases of metastatic melanoma (103 patients). For each patient, either a magnetic resonance imaging (MRI) or computed tomography (CT) scan, collected from routine clinical care, one or multiple (semi-)automatic lesion segmentations, and ground truth labels from a gold standard (e.g., pathologically proven) are available. All datasets are multicenter imaging datasets, as patients referred to our institute often received imaging at their referring hospital. The dataset can be used to validate or develop radiomics methods, i.e., using machine or deep learning to relate the visual appearance to the ground truth labels, and automatic segmentation methods. See also the research article related to this dataset: Starmans et al., Reproducible radiomics through automated machine learning validated on twelve clinical applications, Submitted.View this table:Competing Interest StatementWiro J. Niessen is founder, scientific lead, and shareholder of Quantib BV. Jacob J. Visser is a medical advisor at Contextflow. Astrid A. M. van der Veldt is a consultant (fees paid to the institute) at BMS, Merck, MSD, Sanofi, Eisai, Pfizer, Roche, Novartis, Pierre Fabre and Ipsen. The other authors do not declare any conflicts of interest.Funding StatementThis research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.Author DeclarationsI confirm all relevant ethical guidelines have been followed, and any necessary IRB and/or ethics committee approvals have been obtained.YesThe details of the IRB/oversight body that provided approval or exemption for the research described are given below:The study protocol for the collection of the WORC database conformed to the ethical guidelines of the 1975 Declaration of Helsinki. Approval by the local institutional review board of the Erasmus MC (Rotterdam, the Netherlands) was obtained for collection of the WORC database (MEC-2020-0961), and separately for the six included studies (Lipo: MEC-2016-339, Desmoid: MEC-2016-339, Liver: MEC-2017-1035, GIST: MEC-2017-1187, CRLM: MEC-2017-479, Melanoma: MEC-2019-0693). The need for informed consent was waived due to the use of anonymized, retrospective data.All necessary patient/participant consent has been obtained and the appropriate institutional forms have been archived.YesI understand that all clinical trials and any other prospective interventional studies must be registered with an ICMJE-approved registry, such as ClinicalTrials.gov. I confirm that any such study reported in the manuscript has been registered and the trial registration ID is provided (note: if posting a prospective study registered retrospectively, please provide a statement in the trial ID field explaining why the study was not registered in advance).YesI have followed all appropriate research reporting guidelines and uploaded the relevant EQUATOR Network research reporting checklist(s) and other pertinent material as supplementary files, if applicable.YesThe data referred to in this manuscript is publicly available at https://xnat.bmia.nl/data/projects/worc. The code to download the data and reproduce the experiments from the radiomics study in which this data was presented can be found at https://github.com/MStarmans91/WORCDatabase. https://xnat.bmia.nl/data/projects/worc https://github.com/MStarmans91/WORCDatabase},
	URL = {https://www.medrxiv.org/content/early/2021/08/25/2021.08.19.21262238},
	eprint = {https://www.medrxiv.org/content/early/2021/08/25/2021.08.19.21262238.full.pdf},
	journal = {medRxiv}
}
```

The code to download the WORC database and reproduce our experiments can be found at https://github.com/MStarmans91/WORCDatabase.

## Installation

WORC supports Unix and Windows systems with Python 3.6+: the [unit tests](https://github.com/MStarmans91/WORC/actions?query=workflow%3A%22Unit+test%22)
are performed on the latest Ubuntu and Windows versions with Python 3.7. For detailed installation
instructions, please check  [the ReadTheDocs installation guidelines](https://worc.readthedocs.io/en/latest/static/quick_start.html#installation).

The package can be installed through pip:

      pip install WORC

Alternatively, you can directly install WORC from this repository:

      python setup.py install

Make sure you install the requirements first:

      pip install -r requirements.txt

## 3rd-party packages used in WORC:

 - SimpleITK (Image loading and preprocessing)
 - [Pyradiomics](https://github.com/radiomics/pyradiomics)
 - [PREDICT](https://github.com/Svdvoort/PREDICTFastr)
 - scikit-learn
 - imbalanced-learn
 - xgboost
 - [fastr (Workflow design and building)](http://fastr.readthedocs.io)
 - [ComBat](https://github.com/Jfortin1/ComBatHarmonization) (optional)

See for other python packages the [requirements file](requirements.txt).

## Start
We suggest you start with the [WORC Tutorial](https://github.com/MStarmans91/WORCTutorial).
Besides a Jupyter notebook with instructions, we provide there also an example script for you to get started with.

## Contact
We are happy to help you with any questions. Please sent us a mail or place an issue on the Github.

We welcome contributions to WORC. For the moment, converting your toolbox into a FASTR tool is satisfactory:
see also [the fastr tool development documentation](https://fastr.readthedocs.io/en/stable/static/user_manual.html#create-your-own-tool).

## Optional
Besides the default installation, there are several optional packages you could install to support WORC.

### Graphviz
WORC can draw the network and save it as a SVG image using [graphviz](https://www.graphviz.org/). In order to do so,
please make sure you install graphviz. On Ubuntu, simply run

      apt install graphiv

On Windows, follow the installation instructions provided on the graphviz website.
Make sure you add the executable to the PATH when prompted.

### Elastix
Image registration is included in WORC through [elastix and transformix](http://elastix.isi.uu.nl/).
In order to use elastix, please download the binaries and place them in your
fastr.config.mounts['apps'] path. Check the elastix tool description for the correct
subdirectory structure. For example, on Linux, the binaries and libraries should be in "../apps/elastix/4.8/install/"  and
"../apps/elastix/4.8/install/lib" respectively.

Note: optionally, you can tell WORC to copy the metadata from the image file
to the segmentation file before applying the deformation field. This requires
ITK and ITKTools: see  [the ITKTools github](https://github.com/ITKTools/ITKTools)
for installation instructions.

### XNAT
We use the XNATpy package to connect the toolbox to the XNAT online database platforms. You will only
need this when you use the example dataset we provided, or if you want to download or upload data from or to XNAT. We advise you to specify
your account settings in a .netrc file when using this feature for your own datasets, such that you do not need to input them on every request.
