ns = [16, 64, 256, 512, 1024];
i = 1;
n = ns(i);
m = 2*n;
A = zeros(m,n);
b = zeros(m,1);
save(sprintf('A%d', i),'A');
save(sprintf('b%d', i),'b');
f = [zeros(n,1); 1];
At = [-A, ones(m,1);A,ones(m,1)];
bt = [-b;b];
options = optimoptions('linprog','Algorithm','dual-simplex');
[x, fval, exitflag, output] = linprog(f, At, bt, [], [], zeros(size(f)),[], options)
