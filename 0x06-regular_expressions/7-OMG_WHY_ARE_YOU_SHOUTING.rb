#!/usr/bin/env ruby
string_arg = ARGV[0]

if /[A-Z]/.match?(string_arg)
  matches = string_arg.scan(/[A-Z]/)
  puts "#{matches.join('')}"
else
  puts ""
end
