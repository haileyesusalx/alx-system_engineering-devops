#!/usr/bin/env ruby

log_file = ARGV[0]

File.readlines(log_file).each do |line|
  match_data = line.match(/\[from:(?<sender>.*)\] \[to:(?<receiver>.*)\] \[flags:(?<flags>.*)\]/)
  if match_data
    sender = match_data[:sender]
    receiver = match_data[:receiver]
    flags = match_data[:flags]
    puts "#{sender},#{receiver},#{flags}"
  end
end
