# SummaryDo 



![summarydos](https://user-images.githubusercontent.com/71225087/93237337-a390a500-f788-11ea-954f-a8b8f5b7b729.jpg)




## contents
* The vision
* Summary
* Algorithms 
* Code 
* chrome extension
* design 
* API 
* future look

 

## The vision 


A program that can summarize any product page into small , simple and informatic design with few sentences which can be read or listened to 
in order to help various people during browsing in different ways . 


## summary 


![summary logo](https://user-images.githubusercontent.com/71225087/93217463-c6fc2580-f771-11ea-9a33-df3a6548c8e6.png)



The model will summsrize a web page text after shading it  . post the summarization a voice will read the new text to the browsers enabling 
customers  save : time , efort and help elders or people with disabilties to have the greatest experince .

*  until now it can speak just in  english 


*  the model can deal with alot of pages :

| like : |
| ------------- |
| wikipidia articles    | 
| any item description on amazon    | 
 

ALL just in two clicks    



## Algorithms 

a new algorithm that can summarize in smart way. Which can recognize the product category to result a better summarization to be as much practical as possibble  

* such as :
 if we have a router the model will foucs on specific themes related to the product , in this case (speed , Lan ports ,  technology generation , range)

 likewise on other product (sports, clothing , gaming , furniture , etc ...)  


### TextRank Algorithm
 * (NLP)
which link all the text in the articles then split the hole text into individual senteces . 
Every sentence will find a vector representation . Similarities between sentence vectors are then calculated and stored in a matrix . 

The similarity matrix is then converted into a graph, with sentences as vertices and similarity scores as edges, for sentence rank calculation .
all leads to the final suumary (a certain number of top ranked sentences)


## code

written by python 



 
#### importing the required libraries line [1-5]


* stop_words is a set of default stop words for English language model in spacy which is 
an open source library for (NLP) in python that can be used in deep learning and information extraction (our needs) 

* the string module can help in the event that it contains functions related to strings  

* punctuation is a String of ASCII characters which are considered punctuation characters

* flask for web development issues

* (heapq.nlargest) Return a list with the n largest elements from the dataset




![background](https://user-images.githubusercontent.com/71225087/93233936-56123900-f784-11ea-9b56-937eb796e593.png)

#### line [8- 58] step by step 

* using stop words 
* define a function for summarization (NLP)
* vector represintation of sentences  (extracting)
* creating vectors for the sentences 
* fetchig vectors 
* summary extraction 

#### line [61-84]
* API fitting





## chrome extension 
THe chrome extention was wrriten by javascript and HTML 

the design is simple to satisfy the user experience placing a superb impact 
 
after opening the extension the user will shade the specific text then the new summarized text ready-made to the reader 




## design
The main goal 
* catching attention with preservation to eye relaxation
* simplicity 
* clear typography




 ![summ](https://user-images.githubusercontent.com/71225087/93319473-91f6de00-f818-11ea-87f5-25347656a967.jpg)

color | black & orange | inspired by amazon logo
---|---|---
wording  | killer brief |reader comfort 
logo | matchless | represent the idea 


## API 

it is a computing interface which defines interactions between multiple software in our case a web page and the python program
 using (flask )& (json) we had the potential connecting them together . 

* flask api to connect with frontend   


now the model is able to grab a text from any web page and summarize it to the reader with  voice emulator


so it's readable and hearable    




## future look 

Looking ahead, new trends continue to emerge and merge .
the project development  ( AI & deep learning )  will lead to expantion through every e-commerce web site 
allowing customers enjoying browsing  






![SummaryDo](https://user-images.githubusercontent.com/71225087/93099323-8ee0de00-f6b0-11ea-9a38-010bbf37aca2.jpg)


