function c = f(A,b,x,eps)
    c = sum(((A*x - b).^2 + eps^2).^0.5);
end