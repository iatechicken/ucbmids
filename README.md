# UCB MIDS

Short comprehensive review of my time at UC Berkeley Master of Information and Data Science. Each section is organized by the classes that I took and will include a short samples of codes, screenshots, and links to my work. If any of the links are broken, please let me know at richard.ryu@ischool.berkeley.edu

## W200 Python Fundamental for Data science
### Highlights
- Object Oriented Programming, Functional Programming
- Data Structures
- EDA in Python (pandas, numpy, matpotlib)
- Git (not exactly python but this was important)
- Pseudo-coding
### Mid Term Project: [BBQ Management system](https://github.com/iatechicken/ucbmids/blob/master/W200/BBQ_MGMT_revised.py)
- First python program I ever wrote! A restaurant management application for my friend's Korean BBQ restaurant

  ![home screen](./W200/bbq_1.png)

  ![fridge status](./W200/bbq_2.png)

### Final Project: [Bechdel Analysis](https://docs.google.com/presentation/d/1vHQwoAiBGeFzBr6I7qQ5OstKaOVww4e4v5RFkw12f6o/edit?usp=sharing)

- Used pandas on webscraped data from Box Office Mojo and IMDB

  ![bechdel_highlight](./W200/bechdel.png)

## W203 Statistics for Data Science
### Highlights
- Probability Theory and foundational understanding of classical statistics and how it fits within the broader context of data science

- learned and used R for most assignments

### Final Project: Linear Regression on North Carolina Crime data

- The consulting group Significant Effects, comprised of data scientists Jeff Li, Vasanth Ramani, and Richard Ryu, has been tasked by a political campaign to identify determinants of crime

- [pdf version](./W203/sig_eff.pdf)

- Came up with 3 different linear regression models to predict crime in North Carolina

- Evaluate the models through: CLM assumptions and fit

- ![final results](./W203/final.png)

## W205 Fundamentals of Data Engineering
### Highlights
- First introduction to the world of dockers, cloud services (GCP), data pipeline, query, transformation, and streaming

### Final Project: Instrument an API server to catch and analyze events for a mobile gaming company

- Each weekly assignments build up to the final project where we put it all together in a single data pipeline. Tools and packages leveraged in the final pipeline:

    - dockers
    - Kafka
    - Flask
    - Hadoop HDFS
    - PySpark SQL
    - Pandas, Jupyter Notebook, Numpy

![pipeline architecture](./W205/pipeline.png)

- [step by step annotations](./W205/README.md)

## W209 Data Visualization
### highlights
- Main exposure to D3.js, with general front-end concepts
- Data visualization concepts, theory, etc.
- A picture is worth more than thousand words
- [D3.js examples](https://codepen.io/collection/AGwgrw)

### Final Project: MOSS Dashboard
- Create a dashboard that will visualize the outcome of [LIME](https://github.com/marcotcr/lime)
- [github](https://github.com/jlee-snn/w209_MOSS)
- [Final Presentation] (https://docs.google.com/presentation/d/1LEihVbGMWBkUKJHeLqjL8jqGFBDI-Ceae-GL_Bp2Blw/edit?usp=sharing)

## W207 Applied Machine Learning
### highlights
- My official introduction to Machine Learning. Yes, it took only about a year before I actually got the chance to do Machine Learning. I got a chance to learn from Yacov Salomon and one thing I will remember the most is his whiteboard and always dry markers... and how he always emphasized the importance of understanding the intuition behind any algorithms. To get a better understanding of what I mean, take a look at the Q&A below from one of the assignments:
```
Q: Any ideas why logistic regression doesn't work as well as Naive Bayes?

A: The difference between Naive Bayes and logistic regression is that Naive Bayes assumes independence amongst features while logistic regression looks for relationships between features. Since we're dealing with more than 2,000 features, the logistic regression will perform badly due to complexity. If we want to improve the performance of our logistic regression model, we must reduce the number of features
```
- Heavy Exposure: sklearn, numpy, matplotlib
- Code Sample from Assignments:
![GMM](./W207/gmm.png)

    - I think this is the level of technical expectation, about half way into the program. Many differences and improvements can be noticed from my first python code :D. However, I do want to emphasize that my experience at UCB MIDS would not have been possible without all the positive/constructive participation of my fellow classmates, the TAs, and the instructors. Thank you to everyone.

### Final Project: Kaggle - Facial Keypoint Detection Challenge
- This was my first [Kaggle](https://www.kaggle.com/) competition.

- Used Keras, tensorflow, skimage, sklearn, pandas, numpy, matplotlib, CUDA, CuDNN

- [presentation](https://docs.google.com/presentation/d/1IPMNdfzN4TBaobklF8pnc0rI8l8BjUV2utph3ZmKl4Q/edit?usp=sharing)

- [github](https://github.com/iatechicken/kaggle_rnd/blob/master/FinalProject_FacialKepoints_RnD.ipynb)

![Background](./W207/background.png)

![Architecture](./W207/arch.png)


## W251 Deep Learning in the Cloud at the Edge

## W261 Machine Learning at specialized

## W210 Capstone
