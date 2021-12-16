#saad fareed
from textblob import TextBlob 		#using this library for getting Sentiment of that Sentence
import pandas as pd					#Reading CSV file so using this pandas library



def Sentiment(sentence):			#function Define for calling seprate for specific sentence
	analysis = TextBlob((sentence))			#getting the polarity of that sentence
	if analysis.sentiment.polarity > 0: 			# if polarity is > 0 then its show positive in the sentence
		return str(analysis.sentiment.polarity)+',Positive'		#return the function positive
	elif analysis.sentiment.polarity == 0: 	# if polarity is == 0 then its show neutral in the sentence
		return str(analysis.sentiment.polarity)+',Neutral'		#return the function neutral
	else:									# if polarity is < 0 then its show negative in the sentence
		return str(analysis.sentiment.polarity)+',Negative'		#return the function negative

def stars(mystar):			#function Define for calling seprate for specific sentence

	if mystar > 3: 			# if polarity is > 0 then its show positive in the sentence
		return 'Positive'		#return the function positive
	elif mystar == 3: 	# if polarity is == 0 then its show neutral in the sentence
		return 'Neutral'		#return the function neutral
	else:									# if polarity is < 0 then its show negative in the sentence
		return 'Negative'		#return the function negative



data=pd.read_csv('DarazDataComplete.csv')  #reading the CSV which create on scraping
star=data['AverageRating']
#print(star)
rating=[]
review=data['Review']		#Getting the specific Column of review
review=review.fillna('')	#fill null with Empty String
polaritynumber=[]			#making list for polarity number 	(>0 , <0 , =0)
polarity=[]					#making list for polarity word (negative,positive,neutral) 	
for i in star:			#looping for all reviews one by one
	values=stars(i)
	rating.append(values)

#print(rating)


			#calling the function and getting the sentiment polarity and polaritynumber
for i in star:			#looping for all reviews one by one
	values=Sentiment(i)
	values=values.split(',')		#spliting with ',' so we can sperate both number and polarity
	polaritynumber.append(values[0])	#zero index means polarity value (>0 , <0 , =0)
	polarity.append(values[1])			#one index means polarity word (negative,positive,neutral) 
	
data["Sentiment_result"]=rating
data.to_csv('result.csv',index=False)
data['Review']=review			#saving the review in the Dataframe	
data['PolarityNumber']=polaritynumber		#saving the PolarityNumber in the Dataframe	
data['Polarity']=polarity			#saving the review in the Polarity	

data.to_csv('SentimentDataComplete.csv',index=False)		#saving the dataframe into CSV
