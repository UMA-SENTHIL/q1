formatter = "%{first} %{second} %{third}"
puts formatter %{first:1, second: 2, third: 3}   #formating 123
puts formatter %{first: "one", second: "two", third: "three"}
puts formatter %{first: true, second: false, third: true}
puts formatter %{first: formatter, second: formatter, third: formatter}   
puts formatter %{
first: "There are",
second: "varieties",
third: "fruits in shop"}    #formating various string in different lines