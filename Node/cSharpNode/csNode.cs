using System;

namespace cSharpNode
{
   public class csNode
    {
	private object data;
	private csNode next;

        //constructor for the node
        public csNode(csNode next, object data){
            this.data = data;
            this.next = next;
        }

        //properties for data
        public object Data{
            get { return this.data; }
            set { this.data = value; }
        }

        //properties for next node
        public csNode Next{
            get { return this.next; }
            set { this.next = value; }
        }
    }

	class ProgramEntry
	{
		static void Main(string[] args)
		{
			
		}
	}
}
