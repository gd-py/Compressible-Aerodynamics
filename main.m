clc;
clear;

g = 1.4;
theta = linspace(0, pi/2, 100);
beta = linspace(0, pi/2, 100);
m = 0;

for M1=1:0.2:10
    m = m+1;   
    M1n = M1*sin(beta);
    M1n_star = (1+(g-1)*M1n.^2)/(g*M1n.^2-(g-1)/2);
    value = tan(beta-theta)./tan(beta)-M1n_star;
    theta_beta = find_theta_beta(theta, beta, M1);

end

function vec_pairs = find_theta_beta(theta, beta, M1)
    g = 1.4;
    len_X=length(theta);
    len_Y=length(beta);
    num_pairs=0;
    for i=1:len_X
        for j=1:len_Y
            M1n = M1*sin(beta);
            M1n_star = (1+(g-1)*M1n.^2)/(g*M1n.^2-(g-1)/2);
            value = tan(beta-theta)./tan(beta)-M1n_star;
            if abs(value)<=0.001
               num_pairs=num_pairs+1;
               vec_pairs(num_pairs, :)=[theta(i), beta(j)];
            end
        end
    end
end