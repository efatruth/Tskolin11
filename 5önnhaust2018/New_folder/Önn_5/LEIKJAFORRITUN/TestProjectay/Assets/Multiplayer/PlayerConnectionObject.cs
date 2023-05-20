using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;

public class PlayerConnectionObject : NetworkBehaviour {

	// Use this for initialization
	void Start () {
        //Checks if the object initializing is its own local PlayerConnectionobject and not another player's.
        if ( isLocalPlayer == false)
        {
            PlayerCamera.SetActive(false);
            return;
        }

        Debug.Log("PlayerObject::Start -- Spawning my own personal unit.");

        // Instantiate() only creates an object on the LOCAL computer.
        // Even if it has a NetworkIdentity, it will still NOT exist on
        // the network (and therefore not on any other client) UNLESS
        // Network.Server.Spawn() is called on this object.

        //Instantiate(PlayerCharacterPrefab);
        PlayerCamera.SetActive(true);
        CmdSpawnMyUnit();
	}

    public GameObject PlayerCharacterPrefab;
    public GameObject PlayerCamera;

    // Gets the movementscript for player and places it into this gameobject.
    GameObject myPlayerUnit;


    void Update () {
		// Update runs on EVERYONES computer, regardless of who owns this particular player object.
	}

    ///////////////////// COMMANDS
    // Commands are special functions that ONLY get executed on the server.
    // All commands must start with Cmd.


 

    [Command]
    void CmdSpawnMyUnit()
    {
        // This guarentees that the playerobject gets to be on the server.
        GameObject go = Instantiate(PlayerCharacterPrefab);

        myPlayerUnit = go;

        //go.GetComponent<NetworkIdentity>().AssignClientAuthority(connectionToClient);
        // Now that the object exists on the server, propagate it to all
        // the clients (and also wire up the NetworkIdentity)
        // Spawning with Client authority gives the player control of his own object.

        //NetworkServer.Spawn(go);
        NetworkServer.SpawnWithClientAuthority(go, connectionToClient);
    }

}
