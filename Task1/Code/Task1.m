clear
ns = [16, 64, 256, 512, 1024];
results = zeros(5,6);
for i = 1:5
    n = ns(i);
    m = 2*n;
    load(sprintf('Q1Data/A%d.mat', i));
    load(sprintf('Q1Data/b%d.mat', i));
    A = eval(sprintf('A%d', i));
    b = eval(sprintf('b%d', i));
    
    %Infinity Norm:
    f = [zeros(n,1); 1];
    At = [-A, ones(m,1);A,ones(m,1)];
    bt = [-b;b];
    options = optimoptions('linprog','Algorithm','dual-simplex');
    
    % Note importance of using -At, -bt since linprogs expression is: Ax <= b
    inf = tic;
    x = linprog(f, -At, -bt, [], [], [],[], options);
    time = toc(inf);
    
    x = x(1:n);
    resInf = A*x - b;
    results(i, 3) = norm(resInf, Inf);
    results(i, 3+3) = time;
    if i == 5
        figure
        histogram(resInf)
        title('Histogram of residuals minimising the inf-norm')
        hold on
    end
    
    %One Norm
    f = vertcat(zeros(n, 1), ones(m, 1));
    At = [-A, eye(m);A,eye(m)];
    bt = [-b;b];
    
    one = tic;
    x = linprog(f, -At, -bt, [], [], [],[], options);
    time = toc(one);
    
    x = x(1:n);
    res1 = A*x - b;
    results(i, 1) = norm(res1, 1);
    results(i, 3+1) = time;
    
    if i == 5
        figure
        histogram(res1)
        title('Histogram of residuals minimising the 1-norm')
        hold on
    end
    
    %Two Norm
    two = tic;
    x = linsolve(A, b);
    time = toc(two);
    
    res2 = A*x - b;
    results(i, 2) = norm(res2, 2);
    results(i, 3+2) = time;
    if i == 5
        figure
        histogram(res2)
        title('Histogram of residuals minimising the 2-norm')
        hold on
    end    
    
end