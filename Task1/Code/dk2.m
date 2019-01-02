function dk = dk2(A,b,X,epsilon,gamma)
    [M,N] = size(A);
    dk = zeros(N,1);
    Axb = A*X-b;
    temp = sqrt(sum(Axb.^2));
    for j=1:N
        dk(j,1) = gamma*X(j)/sqrt(X(j,1).^2+epsilon^2);
        for i = 1:M
            dk(j,1)=dk(j,1)+A(i,j)*Axb(i,1)/temp;
        end
    end
end