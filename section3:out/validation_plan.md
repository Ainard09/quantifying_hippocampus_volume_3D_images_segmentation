## Intended Use
The algorithm is designed to assist radiologists to segment volume hippopcampcus in 3D brain MRI scans for longitudinal studies of alzheimer's disease.

## Indication For Use
End-to-end AI system which features a machine learning algorithm that integrates into a clinical-grade viewer(OHIF) and automatically measures hippocampal volumes of new patients brain MRI scans, as their studies are committed to the clinical imaging archive(orthanc).

## Training Data
The dataset was obtained from medical decathlon competition. This dataset is stored as a collection of NIFTI files, with one file per volume, and one file per corresponding segmentation mask(label). The original images here are T2 MRI scans of the full brain. In this dataset we are using cropped volumes where only the region around the hippocampus has been cut out. This makes the size of our dataset quite a bit smaller, our machine learning problem a bit simpler and allows us to have reasonable training times. 

## Quality of Ground Truth
The labels for the corresponding dataset were obtained through rigirous effort from a team of radiology experts thata helped to run a HippoCrop tools which cut a rectangular portion of a brain MRI scans from every series and assisted to segment dataset of relevant volumes which are used to train the model.

## Performance Metrics
We evaluated the algorithm's performance using metrics such as Dice coefficient and Jaccard (IoU) similarity coefficient. Sensitivity and specificity metrics were also utilized to evaluate the model. All metrics indicated that the algorithm achieved a success rate of over 80% in segmentation. Notably, sensitivity and specificity exceeded 95%, demonstrating the algorithm's proficiency in accurately segmenting the volume of the hippocampus and distinguishing it from other brain regions considered as background.
The algorithm will successfully give best accuracy on T2 MRI scans of the brain upon which it was trained on.
