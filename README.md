# news_generator

This is a small microservice for ricknmorty app. This microservice uses GPT-2 neural network pretrained model to generate different fictional news about 'Rick and Morty'. 
I've used GPT-2, not my own model, as it's faster and much more convenient.


So news are being generated every 1 or 2 minutes and you can fetch them using endpoint '/latest-news'. 
This news will be used after in rick_and_morty_be and in mobile app.
