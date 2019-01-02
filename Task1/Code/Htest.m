function H = Htest(A,x,b,eps)
    [M,N] = size(A);
    H = zeros(N);
    Axb = A*x - b;
    for i = 1:N
        for j = 1:N
            for k = 1:M
                H(i,j)=H(i,j)+(A(k,i)*A(k,j)*eps^2*(Axb(k,1)^2+eps^2)^(-1.5));
            end
        end
    end
end