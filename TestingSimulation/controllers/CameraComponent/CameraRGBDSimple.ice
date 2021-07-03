//******************************************************************
// 
//  Generated by RoboCompDSL
//  
//  File name: CameraRGBDSimple.ice
//  Source: CameraRGBDSimple.idsl
//
//******************************************************************
#ifndef ROBOCOMPCAMERARGBDSIMPLE_ICE
#define ROBOCOMPCAMERARGBDSIMPLE_ICE
module RoboCompCameraRGBDSimple
{
	exception HardwareFailedException{ string what; };
	sequence <byte> ImgType;
	sequence <byte> DepthType;
	struct TImage
	{
		int cameraID;
		int width;
		int height;
		int depth;
		int focalx;
		int focaly;
		int alivetime;
		ImgType image;
	};
	struct TDepth
	{
		int cameraID;
		int width;
		int height;
		int focalx;
		int focaly;
		int alivetime;
		float depthFactor;
		DepthType depth;
	};
	struct TRGBD
	{
		TImage image;
		TDepth depth;
	};
	interface CameraRGBDSimple
	{
		TRGBD getAll (string camera) throws HardwareFailedException;
		TDepth getDepth (string camera) throws HardwareFailedException;
		TImage getImage (string camera) throws HardwareFailedException;
	};
};

#endif
