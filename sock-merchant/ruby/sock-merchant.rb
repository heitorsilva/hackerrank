#!/bin/ruby

require 'json'
require 'stringio'

def sockMerchant(n, ar)
  ar.group_by{|i| i}.map{|k,v| [k, v.count] }.reduce(0){|sum, sock| sock[1] % 2 == 0 ? sum + sock[1] / 2 : sum + (sock[1]-1) / 2 }
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

n = gets.to_i

ar = gets.rstrip.split(' ').map(&:to_i)

result = sockMerchant n, ar

fptr.write result
fptr.write "\n"

fptr.close()
