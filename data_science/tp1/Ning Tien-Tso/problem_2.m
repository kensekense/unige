
%Problem 2-1
A = [3 5 -5;-5 -7 5;-5 -5 3];
P = [-1 1 -1;1 0 1;1 1 0];
det_a = det(A);
eig_a = eig(A);
[V,D] = eig(A);
disp(A);
disp(P);
disp(eig_a);
q = P*diag([3 -2 -2])-A*P; % PLAMBA - AP = 0
disp(q); %this shows the eigendecomposition is sucessful

%Problem 2-3

%compute the covariance matrix
cov0 = cov(data);
cov1 = cov(data1);
cov2 = cov(data2);
cov3 = cov(data3);
cov4 = cov(data4);
%compute the eigenvalues for covariance matrix
e0 = eig(cov0);
e1 = eig(cov1);
e2 = eig(cov2);
e3 = eig(cov3);
e4 = eig(cov4);
%compute the determinant for covariance matrix
det0 = det(cov0);
det1 = det(cov1);
det2 = det(cov2);
det3 = det(cov3);
det4 = det(cov4);
%compute product of eigenvalues for covariance matrix
prod0 = prod(e0);
prod1 = prod(e1);
prod2 = prod(e2);
prod3 = prod(e3);
prod4 = prod(e4);
%display the eigenspectrum
espec0 = eigs(cov0, 100);
espec1 = eigs(cov1, 100);
espec2 = eigs(cov2, 100);
espec3 = eigs(cov3, 100);
espec4 = eigs(cov4, 100);
x =[1:100];
plot(x, espec0); %change the espec value to get the corresponding graph
title('Eigenspectrum');
xlabel('Rank');
ylabel('Eigenvalue');

%Problem 3

%distance calculation done by hand
x = [0,2;10,5];
y = [3,6;18,4];
plot(x,y, 'Marker', 'o'), axis([0 10 0 10]);