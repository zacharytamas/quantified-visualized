# quantified-visualized

The server for visualizing my life through the data I collect in the `quantified-data` repository.

## Model planning

Here are the AppEngine models I think I'll be making at this point:

- `BatteryLevel (_id, datetime, battery_level)` Reporter is tracking the battery level of my phone every time I report, so why not collect this data? Perhaps make a graph of my battery levels throughout the day to see if that's insightful. Or see how long on average I go before I charge my phone (where two contiguous reports where the second has a higher battery level must mean I charged)
- `Altitude` Again, why not? Reporter keeps this data.
- `Weather` This one has a lot of potential. Reporter saves a TON of information about the weather during your reports. This could be used for fun (how many sunny vs cloudy days did I have) or for more meaningful insights such as how is my mood affected by weather.
- `Audio` Just a record of audio levels around me. Not sure of usage.
- `Location` Obviously a lot can be gleaned from here. My most common places, travel, etc.
- `Food` This one is not provided by Reporter, obviously, but I have specific questions at the end of the day such as "What did you have for dinner?" which may offer insights as to my nutrition, favorite foods, eating habits. Correlated with my weight, of course, would be an interesting vector.

**More coming.** I'm just starting to really think about this.
