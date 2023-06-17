# Report to the Clinicians

Alzheimer's Disease (AD) is a progressive neurodegenerative disorder that leads to neuronal impairment in the brain cells. It is a common cause of dementia, characterized by memory loss. The hippocampus, located in the medial temporal lobe of the brain, is typically affected by this disease.

For patients exhibiting early symptoms, accurately quantifying disease progression over time through longitudinal studies can aid in directing therapy and disease management. However, this task can be challenging since each slice of the MRI 3D scans needs to be analyzed, and the shape of the hippocampus structure is not uniform, making the process time-consuming. Time is crucial for patients, and healthcare clinicians prioritize it in the healthcare sector.

The advent of Artificial Intelligence (AI) has prompted my team and me at Udacity to assist clinicians, particularly radiologists, in the semantic segmentation of hippocampus volumes using machine learning. This approach improves workflow efficiency and enables radiologists to focus on areas of interest.

Our AI algorithm takes MRI 3D volumes as input and performs simultaneous segmentation of the hippocampus volumes across anterior and posterior planes. We evaluated the algorithm's performance using metrics such as Dice coefficient and Jaccard (IoU) similarity coefficient. Sensitivity and specificity metrics were also utilized to evaluate the model. All metrics indicated that the algorithm achieved a success rate of over 80% in segmentation. Notably, sensitivity and specificity exceeded 95%, demonstrating the algorithm's proficiency in accurately segmenting the volume of the hippocampus and distinguishing it from other brain regions considered as background.

Harnessing the vast potential of AI in healthcare to aid clinicians in managing and treating Alzheimer's Disease is an immensely rewarding achievement.