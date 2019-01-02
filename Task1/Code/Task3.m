load('Q1Data/A5.mat')
load('Q1Data/b5.mat')
eps = 0.001;
gamma = 2.223;
x = graddesctask3(A5,b5,eps,gamma);
sparsity = find(abs(x)>eps);
card = size(sparsity,1);
Asparse = A5(:, sparsity);
xstar = linsolve(Asparse, b5);