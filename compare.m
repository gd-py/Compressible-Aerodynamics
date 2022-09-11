clc;
clear;

function [vec_pairs, num_pairs] = find_greater(X, Y)
len_X=length(X);
len_Y=length(Y);
num_pairs=0;   %   number of such pairs that have been found
for i=1:len_X
    for j=1:len_Y
        z=f(X(i), Y(j));    %    insert name of your function, as defined in another .m file
        if z>0
           num_pairs=num_pairs+1;
           vec_pairs(num_pairs, :)=[X(i), Y(j)];
        end
    end
end
end