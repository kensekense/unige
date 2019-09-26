clear
clc
format long

a = [2;5];
b = [6;4];
plot(a,b), axis([0 10 0 10]); %this plots the vector on the x,y coordinate for reference

x = [2;6];
y = [5;4];
z = x-y;
d = sqrt(sum((x-y).^2)); %this shows the euclidean distance as per the formula
sp = sqrt(sum(z.*z)); %shows scalar product
d2 = norm(x-y); %this shows that the distance is the norm (magnitude) of the vector (x,y)
