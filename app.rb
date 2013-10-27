require 'sinatra'

require 'mongo'
require 'json/ext' 

include Mongo


configure do
	conn = MongoClient.new("localhost", 27017)
	set :mongo_connection, conn
	set :mongo_db, conn.db('quantum')
end

get '/tweets' do
  content_type :json
  settings.mongo_db['tweets'].find.to_a.to_json
end
