*****
WORC: Workflow for Optimal Radiomics Classification
*****

Welcome to the WORC documentation!
---------------------------------------------

WORC is an open-source python package for the fully automatic execution of end-to-end
radiomics pipelines. Using automated machine learning, WORC automatically determines the optimal combination
from a wide variety of radiomics methods and parameters to develop a radiomics model on your dataset. Thereby, performing
a radiomics study is effectively reduced to a black box with a push button, where you simply have to input
your data and WORC will adapt the workflow to your application. Thus, WORC is especially suitable
for the fast development of signatures and probing datasets for new biomarkers.

.. note:: Despite the name, besides classification, WORC can actually also be
   used for regression and multilabel classification. See for more details the
   :ref:`additonalfunctionality-chapter` chapter.

We aim to establish a general radiomics platform supporting easy
integration of other tools. With our modular build and support of
different software languages (Python, MATLAB, R, executables etc.), we want
to facilitate and stimulate collaboration, standardisation and
comparison of different radiomics approaches. By combining this in a
single framework, we hope to find an universal radiomics strategy that
can address various problems.

WORC is open-source (licensed under the Apache 2.0 license) and hosted on Github at `https://github.com/MStarmans91/WORC <https://github.com/MStarmans91/WORC>`_

For support, go to the issues on the Gibhub page: `https://github.com/MStarmans91/WORC/issues <https://github.com/MStarmans91/WORC/issues>`_

To get yourself a copy, see the :ref:`installation-chapter` chapter.

The official documentation can be found at `WORC.readthedocs.io <http://WORC.readthedocs.io>`_.

For Tutorials on WORC, both for beginner and advanced WORCflows, please
see our Tutorial repository https://github.com/MStarmans91/WORCTutorial.

For more information regarding radiomics, we recommend the following book chapter:

    `M. P. A. Starmans, S. R. van der Voort, J. M. Castillo T., J. F. Veenland, S. Klein, W. J. Niessen. "Radiomics: Data mining using quantitative medical image features" Handbook of Medical Image Computing and Computer Assisted Intervention (MICCAI) 2020 <https://www.sciencedirect.com/science/article/pii/B9780128161760000235/>`_

The article on WORC is currently in preparation. WORC among others has been
presented at the following conferences:

    `M. P. A. Starmans. "Multicentre studies for more robust radiomics signatures." European Congress of Radiology (ECR) 2021: E³ 422 - Radiomics: principles and applications. <https://connect.myesr.org/course/radiomics-principles-and-applications-2/>`_

    `M. P. A. Starmans. "Multicentre studies for more robust radiomics signatures." European Congress of Radiology (ECR) 2020: E3 420-4 Radiomics: principles and applications. <https://connect.myesr.org/course/radiomics-principles-and-applications/>`_

    `M. P. A. Starmans, S. R. van der Voort, M. Vos, F. Incekara, J. J. Visser, M. Smits, M. G. Thomeer, W. J. Niessen and S. Klein. "Fully automatic construction of optimal radiomics workflows." European Congress of Radiology (ECR) 2019. <https://youtu.be/iDUCIxw0D4I/>`_

    `M. P. A. Starmans, R. Miclea, S. R. van der Voort, W. J. Niessen, S. Klein and M. G. Thomeer. "Classification of malignant and benign liver tumours using a radiomics approach." European Congress of Radiology (ECR) 2019. <https://youtu.be/69hK59w28Gw/>`_

    `M. P. A. Starmans, A. Blazevic, S. R. van der Voort, T. Brabander, J. Hofland, W. J. Niessen, W. W. de Herder and S. Klein. "Prediction of surgery requirement in mesenteric fibrosis on CT using a radiomics approach." European Congress of Radiology (ECR) 2019. <https://youtu.be/8GkBBPQ4UxA/>`_

    `M. P. A. Starmans, S. R. van der Voort, R. L. Miclea, M. Vos, F. Incekara, M. J. M. Timbergen, M. M. J. Wijnenga, G. A. Padmos, G. H. J. van Leenders, G. Kapsas, M. J. van den Bent, A. J.P.E. Vincent, D. J. Grünhagen, C. Verhoef, S. Sleijfer, J. J. Visser, M. Smits, M. G. Thomeer, W. J. Niessen, S. Klein. "Harmonizing radiomics among applications through adaptive workflow optimization." European Society of Medical Imaging Informatics (EuSoMII) Annual Meeting 2019. <https://www.eusomii.org/events/eusomii-annual-meeting-2018/>`_

WORC has among others been used in the following studies:

    `L. Angus, M. P. A. Starmans, A. Rajicic, A. E. Odink, M. Jalving, W. J. Niessen, J. J. Visser, S. Sleijfer, S. Klein, A. A. M. van der Veldt. "The BRAF P. V600E Mutation Status of Melanoma Lung Metastases Cannot Be Discriminated on Computed Tomography by LIDC Criteria nor Radiomics Using Machine Learning." Journal of Personalized Medicine 2021 <https://www.mdpi.com/1056234>`_

    `J. M. Castillo T., M. Arif, W. J. Niessen, S. Klein, C. H. Bangma, I. G. Schoots, J. F. Veenland. "A Multi-Center, Multi-Vendor Study to Evaluate the Generalizability of a Radiomics Model for Classifying Prostate Cancer: High Grade vs. Low Grade." Diagnostics 2021 <https://www.mdpi.com/2075-4418/11/2/369>`_

    `M. P. A. Starmans, M. J. M. Timbergen, M. Vos, M. Renckens, D. J. Grünhagen, G. J. L. H. van Leenders, R. S. Dwarkasing, F. J. A. Willemssen, W. J. Niessen, C. Verhoef, S. Sleijfer, J. J. Visser,  S. Klein. "Differential diagnosis and molecular stratification of gastrointestinal stromal tumors on CT images using a radiomics approach". arXiv preprint arXiv:2010.06824 <https://arxiv.org/abs/2010.06824>`_

    `M. J. M. Timbergen, M. P. A. Starmans, M. Vos, G. A. Padmos, D. J. Grünhagen, G. J. L. H. van Leenders, D. Hanff, C. Verhoef, W. J. Niessen, S. Sleijfer, S. Klein, J. J. Visser. "Differential diagnosis and mutation stratification of desmoid-type fibromatosis on MRI using radiomics." European Journal of Radiology 2020 <https://doi.org/10.1016/j.ejrad.2020.109266>`_

    `M. P. A. Starmans, F. E. Buisman, S. R. van der Voort, D. J. Grünhagen, P. B. Vermeulen, C. Verhoef, S.Klein, J.J. Visser. "Prediction of histopathological growth patterns by radiomics and CT-imaging in patients with operable colorectal liver metastases: a proof-of-concept study." European Congress of Radiology (ECR) 2020 <https://insightsimaging.springeropen.com/articles/supplements/volume-11-supplement-1/>`_

    `M. Vos, M. P. A. Starmans, M. J. M Timbergen, S. R. van der Voort, G. A. Padmos, W. Kessels, W. J. Niessen, G. J. L. H. van Leenders, D. J. Grünhagen, S. Sleijfer, C. Verhoef, S. Klein, J. J. Visser. "Radiomics approach to distinguish between well differentiated liposarcomas and lipomas on MRI" British Journal of Surgery 2019 <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6899528/>`_

    `J. M. Castillo T., M. P. A. Starmans, I. Schoots, W. J. Niessen, S. Klein, J. F. Veenland. "CLASSIFICATION OF PROSTATE CANCER: HIGH GRADE VERSUS LOW GRADE USING A RADIOMICS APPROACH." IEEE International Symposium on Biomedical Imaging (ISBI) 2019. <https://embs.papercept.net/conferences/conferences/ISBI19/program/ISBI19_ContentListWeb_3.html>`_

    `M. P. A. Starmans, R. Miclea, S. R. van der Voort, W. J. Niessen, M. G. Thomeer and S. Klein. "Classification of malignant and benign liver tumors using a radiomics approach." Proceedings Volume 10574, Medical Imaging 2018: Image Processing; 105741D (2018) . <https://doi.org/10.1117/12.2293609>`_

WORC is made possible by contributions from the following people: Martijn P. A. Starmans, Sebastian R. van der Voort, Thomas Phil, and Stefan Klein


WORC Documentation
===================
.. toctree::
    :maxdepth: 3
    :glob:

    static/introduction.rst
    static/quick_start.rst
    static/user_manual.rst
    static/configuration.rst
    static/features.rst
    static/additionalfunctionality.rst
    static/faq.rst
    static/developerdocumentation.rst
    static/file_description.rst
    static/changelog.rst

WORC User reference
====================

.. toctree::
    :maxdepth: 3
    :glob:

    user_reference/*

WORC Developer Module reference
================================
.. toctree::
   :maxdepth: 4

   autogen/WORC



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
