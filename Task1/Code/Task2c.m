eps = logspace(-1, -3);
times = zeros(size(eps));
norms = zeros(size(eps));
load('Q1Data/A1.mat')
load('Q1Data/b1.mat')
for i = 1:size(eps,2)
    [x, ~, ~, times(i)] = graddesc(A1, b1, eps(i));
    norms(i) = f(A1, b1, x, eps(i));
end
plot(eps, times)
title('Effect of epsilon on runtime')
xlabel('epsilon')
ylabel('time')
figure
plot(eps, norms)
title('Effect of epsilon on norm approximation')
xlabel('epsilon')
ylabel('residual norm approximation')