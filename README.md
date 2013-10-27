# quantum

**quant·um**  */ˈˈkwɒntəm/*

*Noun:*  
a required or allowed amount, especially an amount of money legally payable in damages

*Synonyms:*	
amount, portion, total, measure, sum, unit

![Announce all the Tweets!!!!!!!](http://f.cl.ly/items/3d060M1c0K3v1g0T0W2F/1315118240688.jpg "Announce all the Tweets!!!!!!!")

## Description

I joined [twitter](http://www.twitter.com) on 1st March 2007, however my first [tweet](https://twitter.com/swmcc/statuses/841174273) was on the 22nd Jun 2008 and my 10,000 [tweet](https://twitter.com/swmcc/status/387510042020151296) was on the 8th October 2013.

There are probably tools out there that analyse your twitter [archive](https://blog.twitter.com/2012/your-twitter-archive) however I want to hack at this in my spare time.

This app will take my tweets, guff it into a [MongoDB](http://www.mongodb.org/) database and then run various stats on it and output them in various formats.

## Development Info

```
git clone git remote add origin https://github.com/swmcc/quantum.git
[get your twitter archive and] mv ~/wheverever/data data
cd quantum
bundle install
ruby scripts/read_tweets.rb
ruby app.rb
```

## Todo

  - Install highcharts, d3
  - Add to the API 
  - Add tests

## Notes

This is my main project for the next two weeks (as of 20th October 2013). I envisage this app taking me the guts of two weeks part time to get up and running with my other commitments.  
