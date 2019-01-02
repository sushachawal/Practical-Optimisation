function out = ftask3(A,b,x,eps,gamma)
    out = norm(A*x - b) + gamma*sum(sqrt(x.^2+eps^2));
end