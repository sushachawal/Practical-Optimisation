function gf = gradftask3(A,b,x,eps,gamma)
    gf = (A'*A*x - A'*b)./(norm(A*x - b)) + gamma * 1./sqrt(x.^2 + eps^2) .* x;
end