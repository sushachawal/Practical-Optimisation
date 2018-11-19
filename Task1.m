ns = [16, 64, 256, 512, 1024];
for i = 1:5
    n = ns(i);
    m = 2*n;
    load(sprintf('Q1Data/A%d.mat', i));
    load(sprintf('Q1Data/b%d.mat', i));
    A = eval(sprintf('A%d', i));
    b = eval(sprintf('b%d', i));
    f = [zeros(n,1); 1];
    At = [-A, ones(m,1);A,ones(m,1)];
    bt = [-b;b];
    options = optimoptions('linprog','Algorithm','dual-simplex');
    
    % Note importance of using -At, -bt since linprogs expression is: Ax <= b
    [x, fval, exitflag, output] = linprog(f, -At, -bt, [], [], [],[], options)
end