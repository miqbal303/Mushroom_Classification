# Mushroom_Classification

**Problem Statement:**
The Audubon Society Field Guide to North American Mushrooms contains descriptions
of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom (1981). Each species is labelled as either definitely edible, definitely poisonous, or maybe edible but not recommended. This last category was merged with the toxic category. The Guide asserts unequivocally that there is no simple rule for judging a mushroom's edibility, such as "leaflets three, leave it be" for Poisonous Oak and Ivy.

This project aims to develop a machine-learning algorithm to accurately classify mushrooms as either 'edible' or 'poisonous' based on their specifications like cap shape, cap-surface, bruises, odor, cap color, gill color, etc. utilizing various classifiers and supervised learning techniques.

---

Attribute Information: (classes: edible=e, poisonous=p)

* cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s
* cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s
* cap-color: brown=n,buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y
* bruises: bruises=t,no=f
* odor: almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s
* gill-attachment: attached=a,descending=d,free=f,notched=n
* gill-spacing: close=c,crowded=w,distant=d
* gill-size: broad=b,narrow=n
* gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y
* stalk-shape: enlarging=e,tapering=t
* stalk-root: bulbous=b,club=c,cup=u,equal=e,rhizomorphs=z,rooted=r,missing=?
* stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s
* stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s
* stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y
* stalk-color-below-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y
* veil-type: partial=p,universal=u
* veil-color: brown=n,orange=o,white=w,yellow=y
* ring-number: none=n,one=o,two=t
* ring-type: cobwebby=c,evanescent=e,flaring=f,large=l,none=n,pendant=p,sheathing=s,zone=z
* spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r,orange=o,purple=u,white=w,yellow=y
* population: abundant=a,clustered=c,numerous=n,scattered=s,several=v,solitary=y
* habitat: grasses=g,leaves=l,meadows=m,paths=p,urban=u,waste=w,woods=d
* The dataset has 8,124 rows and 23 features included target.
* Dataset has only categorical data.
* The target variable determines whether a mushroom is classified as "edible" or "poisonous" based on its toxicity.

## Architecture Flow

![1690649324528](image/README/1690649324528.png)



## EDA

* In the given dataset, the 'Veil Type' feature has only one category and is not included as it does not contribute to the classification task, likely because all mushrooms in the dataset have the same 'Veil Type.'
* The 'stalk-root' feature in the dataset contains '?' symbols, which are replaced with 'None,' and any missing values are filled with the mode of the feature.

##### Visualization

![1690569053862](image/README/1690569053862.png)

![1690569063116](image/README/1690569063116.png)![1690569070664](image/README/1690569070664.png)![1690569075652](image/README/1690569075652.png)![1690569106062](image/README/1690569106062.png)![1690569112278](image/README/1690569112278.png)![1690569121494](image/README/1690569121494.png)![1690569138024](image/README/1690569138024.png)![1690569145919](image/README/1690569145919.png)![1690569161483](image/README/1690569161483.png)![1690569167950](image/README/1690569167950.png)![1690569204541](image/README/1690569204541.png)![1690569219776](image/README/1690569219776.png)![1690569230209](image/README/1690569230209.png)![1690569247800](image/README/1690569247800.png)![1690569261915](image/README/1690569261915.png)![1690569275036](image/README/1690569275036.png)![1690569306399](image/README/1690569306399.png)![1690569314527](image/README/1690569314527.png)![1690569323475](image/README/1690569323475.png)![1690569348944](image/README/1690569348944.png)![1690569366256](image/README/1690569366256.png)![1690569379239](image/README/1690569379239.png)![1690569391259](image/README/1690569391259.png)

Corelation

![1690569477154](image/README/1690569477154.png)

## Model_Training

**80% of the dataset was used for training the machine learning algorithm, and the remaining 20% was used for testing and evaluating its performance.**

#### I have used the following classification methods:

* **Logistic Regression Classifier**

![1690569906939](image/README/1690569906939.png)![1690569923591](image/README/1690569923591.png)

* **Random Forest Classifier**

![1690569943233](image/README/1690569943233.png)![1690569952490](image/README/1690569952490.png)

* **Gradient Boosting Classifier**

![1690569969264](image/README/1690569969264.png)![1690569988520](image/README/1690569988520.png)

* **Support Vector Machine**

  ![1690570110195](image/README/1690570110195.png)![1690570116121](image/README/1690570116121.png)
* **XGB Classifier**

![1690570146692](image/README/1690570146692.png)![1690570151312](image/README/1690570151312.png)

* **Accuracy and Auc-Roc Score of Models**

![1690570494365](image/README/1690570494365.png)![1690570863347](image/README/1690570863347.png)

**Our tuned classification models all performed really well with the dataset.But Among the five models (Logistic Regression, Random Forest, Support Vector Machine, GradientBoosting Classifier, and XGB Classifier), the Random Forest model was identified as the best-performing model for the given task.**

## WEB Application

Using Flask for the user interface, the web-based application accepts all mushroom features as input and provides a quick assessment of whether the mushroom is poisonous or edible.

* Home Page

![1690571363813](image/README/1690571363813.png)

* **Input Page(Test1)**
  ![1690571488478](image/README/1690571488478.png)
* **Output1**

![1690571532616](image/README/1690571532616.png)

* **Input Page(Test2)**

![1690571563260](image/README/1690571563260.png)

* **Output2**

![1690571594737](image/README/1690571594737.png)

## Tools Used

The tools used to build the model include Python with libraries like NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, and Flask was utilized as the web framework.

![1690572335076](image/README/1690572335076.png)
