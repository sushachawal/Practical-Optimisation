for i =1:5    
    load(sprintf('Q1Data/A%d.mat', i));
    load(sprintf('Q1Data/b%d.mat', i));
end
[xnewt, internewt,~, timenewt] = newton(A2, b2, 0.01);
[xgrad, intergrad, ~, timegrad] = graddesc(A2, b2, 0.01);
semilogx(internewt, 'r')
hold on
semilogx(intergrad, 'b')
title('Residual reduction for newton and gradient methods')
xlabel('Iteration')
ylabel('Cost function')
grid on
legend('Newton Method','Gradient Descent')
timesnewton = zeros(5,1);
timesnewton(2) = timenewt;
iterationsnewton = zeros(5,1);
iterationsnewton(2) = length(internewt);
timesgrad = zeros(5,1);
timesgrad(2) = timegrad;
iterationsgrad = zeros(5,1);
iterationsgrad(2) = length(intergrad);
finalcosts = zeros(5,1);
finalcosts(2) = internewt(length(internewt));
xoutgrad = {5,1};
xoutgrad{2} = xgrad;
xoutnewt = {5,1};
xoutnewt{2} = xnewt;
for i = [1,3,4,5]
    A = eval(sprintf('A%d', i));
    b = eval(sprintf('b%d', i));
    [xoutnewt{i}, internewt,~, timesnewton(i)] = newton(A, b, 0.01);
    fprintf('Finished newton for %d', i)
    [xoutgrad{i}, intergrad, ~, timesgrad(i)] = graddesc(A, b, 0.01);
    fprintf('Finished grad for %d', i)
    iterationsnewton(i) = length(internewt);
    iterationsgrad(i) = length(intergrad);
    finalcosts(i) = internewt(length(internewt));
end
