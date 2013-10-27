#!/usr/bin/env ruby

require 'date'
require 'JSON'
require 'mongo'
require 'time'
require 'yaml'

# Remove the first and last line from each json file
def remove_lines(str, n)
   res = ""
   arr = str.split("\n")[n..(str.size-n)]
   arr.each { |i| res.concat(i + "\n")  }
   return res
end

# Connect to the db and create a collection
db = Mongo::Connection.new.db("quantum")
tweets_collection = db.collection("tweets")

# Read all the files from the data archive
files = Dir.glob(File.join('data/js/tweets', "*.js"))

# Every file should contain JSON 
files.each do |filename|
	puts "Processing " + filename
	tweets = JSON.parse(remove_lines(open(filename).read, 1))

	tweets.each do |tweet|
		tweets_collection.insert(tweet)
	end
end



