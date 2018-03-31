function [fitresult, gof] = createFit(T, C)


[xData, yData] = prepareCurveData( T, C );

% Set up fittype and options.
ft = fittype( 'b*T^3 + ((0.5036*g/T)^2)*exp(0.5036*g/T)/(1+exp(0.5036*g/T))^2', 'independent', 'T', 'dependent', 'C' );
opts = fitoptions( 'Method', 'NonlinearLeastSquares' );
opts.Display = 'Off';
opts.StartPoint = [0.810633455615081 0.8002804688888];

% Fit model to data.
[fitresult, gof] = fit( xData, yData, ft, opts );

% Plot fit with data.
figure( 'Name', 'Heat Capacity' );
h = plot( fitresult, xData, yData );
legend( h, 'C vs. T', 'Heat Capacity', 'Location', 'NorthEast' );
% Label axes
xlabel T
ylabel C
grid on


