% % Playing with display and random configuration
% config=randomConfiguration(p560);
% show(p560,config);
% xlim([-1.25 1.25]); ylim([-1.25 1.25]); zlim([-0.25 1.75]);
% set(gca,'BoxStyle','full');
% set(gca,'Projection','Orthographic');
% set(gca,'FontSize',16);
% view([130 15]);
% 
% % Interactive GUI
% interactiveGUI=interactiveRigidBodyTree(p560);
% xlim([-1.25 1.25]); ylim([-1.25 1.25]); zlim([-0.25 1.75]);
% set(gca,'BoxStyle','full'); box on
% set(gca,'Projection','Orthographic');
% set(gca,'FontSize',16);
% view([130 15]);
% addConfiguration(interactiveGUI);
% disp(interactiveGUI.StoredConfigurations);
% 
% % How to get back to the home position
% homeCfgStruct = homeConfiguration(p560);
% homeCfg = [homeCfgStruct.JointPosition];
% interactiveGUI.Configuration = homeCfg;

% setting elbow down
p560 = loadrobot("puma560");
config=homeConfiguration(p560);
config(3).JointPosition = 0;
show(p560,config)
xlim([-1.25 1.25]); ylim([-1.25 1.25]); zlim([-0.25 1.75]);
set(gca,'BoxStyle','full');
set(gca,'Projection','Orthographic');
set(gca,'FontSize',16);
view([130 15]);

