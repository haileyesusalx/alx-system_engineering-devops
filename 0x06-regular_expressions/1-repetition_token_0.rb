#!/usr/bin/env ruby
string_arg = ARGV[0]

if /\w/.match?(string_arg)
  puts "#{string_arg}"
else
  puts ""
end
