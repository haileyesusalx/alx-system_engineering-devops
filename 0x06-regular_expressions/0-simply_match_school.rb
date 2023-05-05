#!/usr/bin/env ruby
string_arg = ARGV[0]

if /School.*School/.match?(string_arg)
  matches = string_arg.scan(/School/)
  puts "#{matches.join('')}"
elsif /School/.match?(string_arg)
  puts "School"
else
  puts ""
end
