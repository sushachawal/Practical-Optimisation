function [x, inter, it, time] = newton(A,b,eps)
    it = 0;
    x = zeros(size(A,2), 1);
    tic;
    inter = [];
    while(norm(gradf(A, b, x, eps)) >= 1e-3)
        gf = gradf(A, b, x, eps);
        hess = H(A,b,x,eps);
        [L, ~] = chol(hess,'lower');
        Linv = inv(L);
        if size(Linv,1) < size(hess, 1)
            save('hesserror.mat', 'hess')
            save('Linv.mat','Linv')
        end
        dx = -Linv'*Linv*gf;
        t = backtrack(A,b,x,dx,gf,eps);
        x = x+dx.*t;
        it = it+1;
        inter = [inter; f(A, b, x, eps)];
    end
    time = toc;
    %plot(1:size(inter), inter)
end