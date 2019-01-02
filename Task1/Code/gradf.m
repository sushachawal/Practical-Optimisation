function out = gradf(A,b,x,eps)
    temp = A*x - b;
    out = A'*(temp.*(temp.^2 + eps^2).^(-0.5));
end