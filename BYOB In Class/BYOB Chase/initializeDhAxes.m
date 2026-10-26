function initializeDhAxes

% Begin: Setup for this stand alone version that will NOT go into the GUI.
close all
app.axes_arm = axes;  % Create a new axes and save a handle to it.
app.jointAngles = [0 0 0 0]; % Start at the zero angle position.
% Try other test poses here, e.g. app.jointAngles = [30 45 -60 90];
%  End : Setup for this stand alone version that will NOT go into the GUI.



% Begin: Code that can go into your GUI's StartupFcn.
clc

app.axes_arm.View = [35 20];
app.axes_arm.Visible = 'off';
hold(app.axes_arm, 'on');


app.axes_arm.XLim = [-450 450];
app.axes_arm.YLim = [-450 450];
app.axes_arm.ZLim = [-110 520];


makeStlLink("BYOB_L0.stl", app.axes_arm, [.25 .25 .25]); 
app.link1Patch = makeStlLink("BYOB_L1.stl", app.axes_arm, [112/255 198/255 210/255]);
app.link1Vertices = get(app.link1Patch, 'Vertices')';
app.link1Vertices(4,:) = ones(1, size(app.link1Vertices,2));

app.link2Patch = makeStlLink("BYOB_L2.stl", app.axes_arm, [198/255 172/255 20/255]);
app.link2Vertices = get(app.link2Patch, 'Vertices')';
app.link2Vertices(4,:) = ones(1, size(app.link2Vertices,2));

app.link3Patch = makeStlLink("BYOB_L3.stl", app.axes_arm, [181/255 24/255 35/255]);
app.link3Vertices = get(app.link3Patch, 'Vertices')';
app.link3Vertices(4,:) = ones(1, size(app.link3Vertices,2));

app.link4Patch = makeStlLink("BYOB_L4.stl", app.axes_arm, [122/255 63/255 181/255]);
app.link4Vertices = get(app.link4Patch, 'Vertices')';
app.link4Vertices(4,:) = ones(1, size(app.link4Vertices,2));


set([app.link1Patch app.link2Patch app.link3Patch app.link4Patch], 'EdgeColor', 'none');
light('Parent', app.axes_arm, 'Position', [500 -600 900]);
lighting(app.axes_arm, 'gouraud');

app.tipMarker = plot3(app.axes_arm, 0, 0, 0, 'o', 'MarkerSize', 7, ...
    'MarkerFaceColor', [1 .45 0], 'MarkerEdgeColor', 'k');


updateArm(app);

end

function updateArm(app)

% Create the A homogenous transformation matrices for the given jointAngles
[A1, A2, A3, A4] = create_BYOB_A_matrices(app.jointAngles);

% Use the current A matricies to form the T0_n matricies.
T0_1 = A1;
T0_2 = A1 * A2;
T0_3 = A1 * A2 * A3;
T0_4 = A1 * A2 * A3 * A4;

link1VerticesWRTground = T0_1 * app.link1Vertices;
link2VerticesWRTground = T0_2 * app.link2Vertices;
link3VerticesWRTground = T0_3 * app.link3Vertices;
link4VerticesWRTground = T0_4 * app.link4Vertices;


set(app.link1Patch,'Vertices', link1VerticesWRTground(1:3,:)');
set(app.link2Patch,'Vertices', link2VerticesWRTground(1:3,:)');
set(app.link3Patch,'Vertices', link3VerticesWRTground(1:3,:)');
set(app.link4Patch,'Vertices', link4VerticesWRTground(1:3,:)');


ptTipOnLink4 = [0;0;0;1];
tipWRTground = T0_4 * ptTipOnLink4;
set(app.tipMarker, 'XData', tipWRTground(1), 'YData', tipWRTground(2), 'ZData', tipWRTground(3));
fprintf('Tip at (%.1f, %.1f, %.1f) mm\n', tipWRTground(1), tipWRTground(2), tipWRTground(3));

end
