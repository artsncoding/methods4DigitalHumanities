# Methods4DigitalHumanities

Background information:
Finnish National Gallery consist of three museums: Ateneum Art Museum, Museum of Contemporary Art Kiasma and Sinebrychoff Art Museum. The Finnish national collection is owned by the state and divided between three museums. As stated by their website: “Responsibility for the augmentation and management of the collection is divided between three museums. The Sinebrychoff Art Museum houses old international art from the 14th to the early 19th century, the Ateneum Art Museum has Finnish art up to 1969 as well as international art from the 19th and 20th centuries, and the Museum of Contemporary Art Kiasma is responsible for Finnish and international art from 1960 onwards.”[1]. Their collections include works of art, objects and archive materials. Art historical archive material is stored and managed by the National Gallery´s Collections Department. Finnish National Gallery offers its digitised collections online and their API is publicly available. Collections are also available through Finna and Europeana and through their APIs.

Project:

Our visualizations represent the digitised material from the Finnish National Gallery. These visualisations give some inside of the structure of collections and how much material has been digitised by the Finnish National Gallery.
Our whole group project can be found here:

The map visualization looks into where the donators of items and collections come from. The research question behind the visualization is "Where are the collections in the Finish Nationar Gallery donated from?". 


Working with FNG API:
Dataset of Finnish National Gallery metadata for the whole digitized collection was downloaded from the Finnish National Gallery(FNG) API. 
The dataset was given as Dublin Core JSON, each item in the description set contained: Title of the item, artwork type, identifier, creator, publisher (containing collection and museum), date of creation and date of acquisition, subject of the piece, format, relation to other items and its previous usage in exhibitions. 
The dataset was parsed into two smaller datasets using Python and Regex (Code provided). 
As not all of the information was required, Python was used to parse item title, museum and acquisition date for dataset 1 and item title, museum, collection, and acquisition date for dataset 2. 
Regex was used to extract the year from acquisition time, as the acquisition time was provided in E52 time span format. 
Both datasets were saved in CSV format to be used in visualizations. 

For dataset 2, the metadata provided by the API did not contain all of the required information. This information was acquired by research, as described below. 
The acquired information on the collection type of each collection and the location of the donator of each collection was added to the dataset.

We have divided the objects into different acquisition types based on the way that object or group of objects have entered the collection.
Acquisition types are the following: “hankinta” (purchase), “lahjoitus” (donation), “talletus” (deposition), “testamentattu valtiolle” (devised to government by last will), “testamenttilahjoitus” (devised to the museum by last will), “unknown” and “valtion talletus” (deposited by government). These categories were based on the categorization used by Finnish National Gallery. These categories were found by searching Finnish National Gallery Kokoelmat page for each collection. Information provided on the page of each item contains information on how the item was acquired. If this information was not provided, it was marked as ‘unknown’. 

Geographical information taken from Wikipedia and other internet resources, books and newspaper articles found by googling the name of the collections or donators. Location has been chosen by the place of death of the person named in the collection or last known place of residence or known workplace[3] (for example living artists who have donated their works to museum). If there is two people mentioned in the name of the collection, we have solely taken the first location we could find, assuming that especially couples have most likely lived together. If there two people who have donated to together but who have no other connection, then we have made them their own entries. If location is unknown, we have marked it as “unknown”.

After the names of the locations had been found, the coordinates of each location were found. 
To find the latitude,longitude coordinates of each location name, GoogleSheets tool ezGeocode was used. 
ezGeocode was used to extract the coordinates of each location, and the name of the location and its coordinates were saved into a CSV file for visualization. 

Analysis: 
The analysis shows, that most of donator locations are in Finland. When finding the location data it was found that many donations come from established finnish families who collected art, so even if the items themselves are foreign in origin, they have been donated by Finnish people. 
Some foreign donations exist from locations all around the world including Japan, USA and Benin. These were from artists and teams with some relationship with Finland. For example collection donated from Japan was from a team with an existing relationship with the Finnish artwold, and Benin donation is from an artist who had an exhibition in Finland. 
So it can be said that most of the donations to the museum come from people with an relationship to the museum, either through national heritage as is the case with Finnish donators, or through other links in the art world such as exhibitions in one of the museums. 

Pipeline biases and problems: 
As the donator location data was not available through the FNG API, it had to be searched for as described above. This data is not always accurate, as the details of less famous donators were more difficult to find. Some of the information had to be estimated using for example the last known work location of the donator, or the location of the donators spouse. These decisions which had to be made on how to estimate the location of the donator also introduces bias on the data, and some other researher might have done these decisions differently. 
However, expecially in the case of locations were numerous donators are from, the data gives a good estimation on the range of locations where the donations come from. 
