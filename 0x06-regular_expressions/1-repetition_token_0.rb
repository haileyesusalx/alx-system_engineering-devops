#!/usr/bin/env ruby
string_arg = ARGV[0]

if /hb(t{2,5}n)/.match?(string_arg)
  puts "#{string_arg}"
else
  puts ""
end
