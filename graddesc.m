function [l1norm, it, time] = graddesc(A,b,eps)
    alpha = 0.5;
    beta  = 1;
    it = 0;
    x = zeros(size(A,2), 1);
    %inter = [];
    tic;
    while(norm(gradf(A, b, x, eps)) >= 10e-3)
        gf = gradf(A, b, x, eps);
        while(f(A, b, x-beta.*gf, eps) >= (f(A, b, x, eps) - alpha*beta*norm(gf)^2))
            beta = beta*0.8;
        end
        x = x-gf.*beta;
        it = it+1;
        %inter = [inter; f(A, b, x, eps)];
    end
    time = toc;
    %plot(1:size(inter), inter)
    l1norm = f(A, b, x, eps);
end