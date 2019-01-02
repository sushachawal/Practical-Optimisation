function [x, inter, it, time] = graddesc(A,b,eps)
    alpha = 0.25;
    beta = 0.4;
    t  = 1;
    it = 0;
    x = zeros(size(A,2), 1);
    inter = [];
    tic;
    while(norm(gradf(A, b, x, eps)) >= 1e-3)
        gf = gradf(A, b, x, eps);
        while(f(A, b, x-t.*gf, eps) >= (f(A, b, x, eps) - alpha*t*norm(gf)^2))
            t = t*beta;
        end
        x = x-gf.*t;
        it = it+1;
        inter = [inter; f(A, b, x, eps)];
    end
    time = toc;
    %plot(1:size(inter), inter)
end