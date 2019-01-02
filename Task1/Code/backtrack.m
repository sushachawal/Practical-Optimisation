function t = backtrack(A,b,x,dx,gf,eps)
    alpha = 0.25;
    beta = 0.4;
    t = 1;
    while(f(A, b, x+t.*dx, eps) >= (f(A, b, x, eps) - alpha*t*gf'*dx))
            t = t*beta;
    end
end