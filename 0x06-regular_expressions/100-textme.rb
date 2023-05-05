#!/usr/bin/env ruby

log_file = ARGV[0]

File.readlines(log_file).each do |line|
  if line.match(/^(.*from:|to:|\[flags:)(.*?)\]?$/)
    sender = $2 if line.match(/^.*from:(.*?)\]?$/)
    receiver = $2 if line.match(/^.*to:(.*?)\]?$/)
    flags = $2 if line.match(/^.*\[flags:(.*?)\]?$/)
    puts "#{sender},#{receiver},#{flags}"
  end
end
