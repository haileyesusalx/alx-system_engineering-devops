#!/usr/bin/env ruby
string_arg = ARGV[0]

if /h(b{0,1}tn)/.match?(string_arg)
  puts "#{string_arg}"
else
  puts ""
end
