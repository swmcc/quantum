#!/usr/bin/env ruby

require 'JSON'

# Remove the first and last line from each json file
def remove_lines(str, n)
   res = ""
   arr = str.split("\n")[n..(str.size-n)]
   arr.each { |i| res.concat(i + "\n")  }
   return res
end

def parse_tweet(tweet)

end

files = Dir.glob(File.join('data/js/tweets', "*.js"))

files.each do |filename|
	puts "Processing " + filename
  	
	tweets = JSON.parse(remove_lines(open(filename).read, 1))

	tweets.each do |tweet|
		parse_tweet(tweet)
	end
end



