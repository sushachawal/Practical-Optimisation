function out = H(A,b,x,eps)
    out = zeros(size(A,1),size(A,1));
    for i = 1:size(A, 1)
        ai = A(i, :);
        bi = b(i);
        temp = ai'*x - bi;
        ki = (temp^2 + eps^2)^(-0.5)-(temp^2 + eps^2)^(-1.5)*temp^2;
        out = out + ki.*(ai*ai');
    end
end