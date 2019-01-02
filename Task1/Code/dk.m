function dk1 = dk(A, x, b, eps)
    [M, N] = size(A);
    dk1 = zeros(N,1);
    Axb = A*x-b;
    
    for k = 1:N
        for i=1:M
            dk1(k,1)=dk1(k,1)+(Axb(i,1).^2+eps^2).^(-0.5)*A(i,k)*Axb(i,1);
        end
    end
end