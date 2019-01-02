function x = graddesctask3(A,b,eps,gamma)
    alpha = 0.5;
    t  = 1;
    beta = 0.25;
    x = zeros(size(A,2), 1);
    while(norm(gradftask3(A, b, x, eps, gamma)) >= 1e-5)
        gf = gradftask3(A, b, x, eps, gamma);
        while(ftask3(A, b, x-t.*gf, eps,gamma) >= (ftask3(A, b, x, eps, gamma) - alpha*t*norm(gf)^2))
            t = beta*t;
        end
        x = x-gf.*t;
    end
end