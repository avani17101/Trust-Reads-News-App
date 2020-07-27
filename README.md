## Motivation and Introduction
Often we want to verify whether a news is real/fake and google search the news and get fake websites on top which leads to more confusion. This happens in case of fake news. The news is not contained in trusted sources but is there is fake websites thus they are displayed on top because of googles SEO and word match. Thus it becomes more confusing to verify the genuinity of news when it is fake. 

This project is an attempt to combat this problem by considering a simple fact that if a news is not there in trusted sources it's probably a fake news.

# Trust Reads: Now read from trusted sorrces
An app where user can enter the topic he wants to read on/verify and get links only from trusted news sources. <br>
![Trust Reads](https://github.com/avani17101/ML-models-and-simple-python-codes-deployment-in-webapps/blob/master/trustReads_newsApp/TrustReads.png)


## Methodology
I have written a python script using Google Search library which is given the list of trusted news sources(2 souces for testing purpose here) and deployed it in flask.


## For run
Clone the repo, cd, download dependencies using "npm install" and type "flask run" in cli.


## Future work
This can be made into a chrome extention and can simply we used to filter the search results when we want to verify the genuinity of news.


## Alternative strategy
Showing all results but showing the fake news sites in the search as flagged will serve the similar purpose.
